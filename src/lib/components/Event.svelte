<script>
  export let event;
</script>

<div>
  <h2>{event.name}</h2>
  <div class="text-center my-3">
    <span><strong>时间: </strong>{event.time} </span>
    <span class="ms-3"><strong>地点:</strong> {event.place}</span>
    <span class="badge rounded-pill bg-success"> {event.status}</span>
  </div>
  <div>
    {event.content}
  </div>
</div>
