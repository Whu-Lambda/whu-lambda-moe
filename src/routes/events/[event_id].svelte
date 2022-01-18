<script>
  import Event from '$lib/components/Event.svelte';

  export let event = {
    id: 1,
    name: 'undefined',
    time: '2022-01-18 18:30-20:30',
    place: 'undefined',
    status: 'undefined',
    content: `undefined`
  };
</script>

<div class="row justify-content-center">
  <div class="col-md-8">
    <Event {event} />
  </div>
</div>
