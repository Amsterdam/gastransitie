// Handle all local geojson endpoints
// Handle extracting data (for tables)
import util from './util'

// general data
let buurtCache = {}
let buurtBoundsCache = {}

// geoJson cache, keyed by "buurt" (lives outside of Vuex)
let afwcCache = {}
let mipCache = {}
let energieLabelCache = {}
let renovatieCache = {}
let warmtekoudeCache = {}

let hrCache = {}
let hrBuurtCache = {}
let bagBrkCache = {}

function UnknownHostException (message) {
  this.message = message
  this.name = 'uknownHostException'
}

function getPrivateApiHost () {
  let privateApiHost = ''
  switch (document.location.hostname) {
    case 'localhost':
    case '127.0.0.1':
      privateApiHost = 'http://' + document.location.hostname + ':8000'
      break
    case 'acc.data.amsterdam.nl':
      privateApiHost = 'https://acc.data.amsterdam.nl'
      break
    case 'data.amsterdam.nl':
      privateApiHost = 'https://data.amsterdam.nl'
      break
    default:
      throw new UnknownHostException('Frontend is running on unknown host, cannot access data.')
  }
  return privateApiHost
}

const PRIVATE_DATA_HOST = getPrivateApiHost()

function getUrl (endpoint, buurt = null) {
  return PRIVATE_DATA_HOST + `/gastransitie/api${endpoint}`
}

async function readGeojson (url) {
  const results = await util.readProtectedPaginatedData(
    url,
    util.getGeoJSONData,
    util.getNextPage
  )
  return util.resultsAsGeoJSON(results)
}

async function readJson (url) {
  const results = await util.readProtectedPaginatedData(
    url,
    util.getPaginatedData,
    util.getNextPage
  )
  return results
}

async function readDataJson (url) {
  const results = await util.readProtectedPaginatedData(
    url,
    util.getNormalData,
    util.getNextPage
  )
  // debugger
  return results
}

// Energie transitie specific data endpoints (all paginated GeoJSON)
async function getAfwc (buurt) {
  if (!afwcCache[buurt]) {
    afwcCache[buurt] = readGeojson(getUrl('/afwc/') + `?buurt=${buurt}`)
  }
  return afwcCache[buurt]
}

async function getEnergieLabel (buurt) {
  if (!energieLabelCache[buurt]) {
    energieLabelCache[buurt] = readGeojson(getUrl('/energielabel/') + `?buurt=${buurt}`)
  }
  return energieLabelCache[buurt]
}

// Meerjarig Investerings Programma
async function getMip (buurt) {
  if (!mipCache[buurt]) {
    mipCache[buurt] = readGeojson(getUrl('/mip/') + `?buurt=${buurt}`)
  }
  return mipCache[buurt]
}

async function getRenovatie (buurt) {
  if (!renovatieCache[buurt]) {
    renovatieCache[buurt] = readGeojson(getUrl('/renovatie/') + `?buurt=${buurt}`)
  }
  return renovatieCache[buurt]
}

async function _getAllBuurtBounds () {
  // From Django GEOSGeometry.extent docs:  (xmin, ymin, xmax, ymax). I.e. (lon, lat) coordinates.
  // This project uses Leaflet which uses (lat, lon) coordinates.
  // So from Django we get [W, S, E, N] and Leaflet needs [S, W, N, E]
  let geojson = await readGeojson(getUrl('/buurtbbox/'))
  geojson.features.forEach(
    feature => {
      let [W, S, E, N] = feature.geometry
      buurtBoundsCache[feature.properties.vollcode] = [[S, W], [N, E]]
    }
  )
}

async function getBuurtBounds (buurt) {
  if (!buurtBoundsCache[buurt]) {
    await _getAllBuurtBounds()
  }
  return buurtBoundsCache[buurt]
}

async function getBuurt (buurt) {
  if (!buurtCache[buurt]) {
    buurtCache[buurt] = readGeojson(getUrl('/buurt/') + `?vollcode=${buurt}`)
  }
  return buurtCache[buurt]
}

async function getHr (buurt) {
  // Note: takes landelijk id not Amsterdam style ones
  if (!hrCache[buurt]) {
    hrCache[buurt] = readJson(getUrl('/handelsregister/') + `?buurt_id=${buurt}`)
  }
  return hrCache[buurt]
}

async function getHrBuurt (buurt) {
  // Note: takes landelijk id not Amsterdam style ones
  if (!hrBuurtCache[buurt]) {
    hrBuurtCache[buurt] = readJson(getUrl('/handelsregisterbuurt/') + `?buurt_id=${buurt}`)
  }
  return hrBuurtCache[buurt]
}

async function getWarmtekoude (buurt) {
  if (!warmtekoudeCache[buurt]) {
    warmtekoudeCache[buurt] = readGeojson(getUrl('/warmtekoude/') + `?buurt=${buurt}&page_size=2000`)
  }
  return warmtekoudeCache[buurt]
}

async function getBagBrk (landelijkeCode) {
  if (!bagBrkCache[landelijkeCode]) {
    let url = PRIVATE_DATA_HOST + `/gastransitie/api/bag/${landelijkeCode}/`
    bagBrkCache[landelijkeCode] = readDataJson(url)
  }
  return bagBrkCache[landelijkeCode]
}

async function getJsonByName (name, buurt) {
  let getters = new Map([
    ['afwc', getAfwc],
    ['energielabel', getEnergieLabel],
    ['mip', getMip],
    ['renovatie', getRenovatie],
    ['buurtbounds', getBuurtBounds],
    ['buurt', getBuurt],
    ['handelsregister', getHr],
    ['handelsregisterbuurt', getHrBuurt],
    ['warmtekoude', getWarmtekoude],
    ['bagbrk', getBagBrk]
  ])

  return getters.get(name)(buurt)
}

export default {
  getAfwc,
  getEnergieLabel,
  getMip,
  getRenovatie,
  getJsonByName,
  getBuurtBounds,
  getBuurt,
  getBagBrk,
  PRIVATE_DATA_HOST
}
