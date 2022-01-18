<script>
  import EventCard from '$lib/components/EventCard.svelte';

  export let events = [
    {
      id: 1,
      name: 'undefined',
      time: '2022-01-18 18:30-20:30',
      place: 'undefined',
      status: 'undefined',
      content: `undefined`
    }
  ];
</script>

<div class="row justify-content-center">
  <div class="col-md-8">
    <h4>近期活动</h4>
    {#each events as event, idx (idx)}
      <EventCard {event} />
    {/each}
  </div>
</div>
