<template>
  <div class="text text-sm sm:text-md">
    <div class="w-full mt-2">
      <strong
      ><span class="box" :class="commemoration.colors[0]"
      />
        &nbsp;<span v-html="commemoration.name"></span></strong
      >
      <a
          v-for="link in commemoration.links"
          :key="link"
          :href="link"
          target="_blank"
          class="link bio_link float-right"
      ><small>Biography</small></a
      >&nbsp;
    </div>
    <!--    <div class="w-full mb-2">-->
    <!--      <em>{{ commemoration.rank.formatted_name }}</em>-->
    <!--    </div>-->
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  props: ["commemoration"],
};
</script>
<style>
.bio_link {
  margin-right: 0.5em;
}
</style>
