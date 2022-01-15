<script>
  export let event;
</script>

<div class="mb-5">
  <div class="event-title">
    <a href="/events/{event.id}">
      <h4>{event.name}</h4>
    </a>
  </div>
  <div class="event-meta">
    <span><strong>时间: </strong>{event.time} </span>
    <span><strong>地点:</strong> {event.place}</span>
    <span class="badge rounded-pill bg-success"> {event.status}</span>
    <br />
  </div>
  <div class="event-abstract">
    {event.content}
  </div>
</div>
