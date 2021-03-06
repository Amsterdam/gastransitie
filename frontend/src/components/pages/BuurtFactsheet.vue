<template>
  <div v-if="buurten && buurten.length && buurtData">
    <div class="float-right">
      <pano></pano>
    </div>
    <div>
      <h2>
        Factsheet {{buurtData.naam}}
      </h2>
      <p>Peildatum: {{new Date().toLocaleDateString("NL")}}</p>
    </div>

    <div class="clearfix"></div>

    <div class="cards">
    <card :title="`${buurtData.naam} Algemeen`">
      <div class="row">
        <div class="col-md-6 col-xs-12">
          <buurt-info></buurt-info>
          <sociale-kenmerken></sociale-kenmerken>
          <parkeer-info></parkeer-info>
          <energie-info></energie-info>
        </div>
        <div class="col-md-6 col-xs-12">
          <amsterdam-map :config="buurtMapConfig"></amsterdam-map>
        </div>
      </div>

      <migratie-achtergrond></migratie-achtergrond>
      <waarde-en-inkomen></waarde-en-inkomen>
    </card>

    <card :title="`${buurtData.naam} Gasverbruik per ~25 aansluitingen`">
      <div class="row">
        <div class="col-md-3">
          <img src="https://acc.map.data.amsterdam.nl/maps/energie?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=gas_verbruik&format=image/svg%2Bxml"/>
        </div>
        <div class="col-md-9">
          <amsterdam-map :config="energieMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>

    <card :title="`Woning bezit in ${buurtData.naam}`">
      <woningen-naar-eigendom></woningen-naar-eigendom>
      <woningen-per-corporatie></woningen-per-corporatie>
      <div class="tableHeader">Corporatie bezit (bron AFWC 2017)</div>
      <div class="row">
        <div class="col-md-6 col-xs-12">
          <style-legend :legend="afwcMapConfig.legend" :complete="false"></style-legend>
        </div>
        <div class="col-md-6 col-xs-12">
          <amsterdam-map :config="afwcMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>

    <card :title="`Bouwkundige kenmerken ${buurtData.naam}`">
      <bouwkundige-kenmerken></bouwkundige-kenmerken>
      <woning-oppervlakten></woning-oppervlakten>
    </card>

    <card :title="`Bedrijvigheid in ${buurtData.naam}`">
      <div class="row">
        <div class="col-md-6 col-xs-12">
          <gebruiks-overzicht></gebruiks-overzicht>
        </div>
        <div class="col-md-6 col-xs-12">
          <gevestigde-bedrijven></gevestigde-bedrijven>
        </div>
      </div>
    </card>

    <card :title="`Werkzaamheden in ${buurtData.naam}`">
      <gepland-per-corporatie></gepland-per-corporatie>
      <gepland-per-jaar></gepland-per-jaar>
      <div class="row">
        <div class="col-12">
          <meerjarig-investerings-plan></meerjarig-investerings-plan>
        </div>
        <div class="col-12">
          <amsterdam-map :config="mipMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>

    <card :title="`Gasleidingen Alliander in ${buurtData.naam}`">
      <div class="row">
        <div class="col-4">
          <style-legend :legend="gasAllianderMapConfig.legend"></style-legend>
        </div>
        <div class="col-8">
          <amsterdam-map :config="gasAllianderMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>

    <card :title="`Warmte / Koude net in ${buurtData.naam}`">
      <div class="row">
        <div class="col-4">
          <style-legend :legend="warmteKoudeMapConfig.legend" :complete="false"></style-legend>
        </div>
        <div class="col-8">
          <amsterdam-map :config="warmteKoudeMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>

    <card :title="`Energie labels in ${buurtData.naam}`">
      <div class="row">
        <div class="col-4">
          <style-legend :legend="energieLabelMapConfig.legend"></style-legend>
        </div>
        <div class="col-8">
          <amsterdam-map :config="energieLabelMapConfig"></amsterdam-map>
        </div>
      </div>
    </card>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import { readData } from '@/services/datareader'

import card from '../Layout/Card'

import AmsterdamMap from '../AmsterdamMap'
import afwcMapConfig from '../../../static/afwc-map-config'
import mipMapConfig from '../../../static/mip-map-config'
import buurtMapConfig from '../../../static/buurt-map-config'
import energieMapConfig from '../../../static/gasverbruik-map-config'
import gasAllianderMapConfig from '../../../static/gas-alliander-map-config'
import warmteKoudeMapConfig from '../../../static/warmte-koude-map-config'
import energieLabelMapConfig from '../../../static/energie-label-map-config'

import socialeKenmerken from '../SocialeKenmerken'
import parkeerInfo from '../ParkeerInfo'
import migratieAchtergrond from '../MigratieAchtergrond'

import GeplandPerJaar from '../GeplandPerJaar'
import GeplandPerCorporatie from '../GeplandPerCorporatie'
import WoningenPerCorporatie from '../WoningenPerCorporatie'
import BouwkundigeKenmerken from '../BouwkundigeKenmerken'
import WoningOppervlakten from '../WoningOppervlakten'
import WoningenNaarEigendom from '../WoningenNaarEigendom'
import GebruiksOverzicht from '../GebruiksOverzicht'
import BuurtInfo from '../BuurtInfo'
import EnergieInfo from '../EnergieInfo'
import GevestigdeBedrijven from '../GevestigdeBedrijven'
import MeerjarigInvesteringsPlan from '../MeerjarigInvesteringsPlan'
import WaardeEnInkomen from '../WaardeEnInkomen'
import Pano from '../Pano'
import StyleLegend from '../StyleLegend'

import { clearStats } from '../../services/mapStyle'

export default {
  data () {
    return {
      afwcMapConfig,
      mipMapConfig,
      buurtMapConfig,
      energieMapConfig,
      gasAllianderMapConfig,
      warmteKoudeMapConfig,
      energieLabelMapConfig
    }
  },
  components: {
    WaardeEnInkomen,
    MeerjarigInvesteringsPlan,
    GevestigdeBedrijven,
    BuurtInfo,
    GebruiksOverzicht,
    WoningenNaarEigendom,
    BouwkundigeKenmerken,
    WoningOppervlakten,
    WoningenPerCorporatie,
    GeplandPerCorporatie,
    GeplandPerJaar,
    EnergieInfo,
    Pano,
    StyleLegend,
    parkeerInfo,
    'card': card,
    'amsterdam-map': AmsterdamMap,
    'sociale-kenmerken': socialeKenmerken,
    'migratie-achtergrond': migratieAchtergrond
  },
  methods: {
    ...mapActions({
      setBuurt: 'setBuurt',
      setBuurtData: 'setBuurtData'
    }),
    async loadBuurt (buurt) {
      this.setBuurt(buurt)
      clearStats()
      if (this.buurten) {
        const buurtDetail = this.buurten.find(b => b.vollcode === buurt)
        const url = 'https://api.data.amsterdam.nl/gebieden/buurt/' + buurtDetail.landelijk
        const buurtData = await readData(url)
        this.setBuurtData(buurtData)
      } else {
        this.setBuurtData(null)
      }
    }
  },
  computed: {
    ...mapGetters([
      'buurten',
      'buurt',
      'buurtData'
    ])
  },
  watch: {
    '$route' (to) {
      this.loadBuurt(to.params.buurt)
    },
    'buurten' () {
      this.loadBuurt(this.buurt)
    }
  },
  mounted () {
    this.loadBuurt(this.$route.params.buurt)
  }
}
</script>

<style scoped>
@media print {
  .cards .card:not(:first-child) {
    page-break-inside: avoid;
  }
  .cards .card:first-child {
    margin-top: 25px !important;
  }
}
</style>
