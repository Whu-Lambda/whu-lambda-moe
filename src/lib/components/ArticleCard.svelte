<script>
  export let article;
</script>

<div class="mb-5">
  <div class="post-title">
    <a href="/articles/{article.id}">
      <h4>{article.name}</h4>
    </a>
  </div>
  <div class="post-meta">
    <span><strong>作者: </strong>{article.author} </span>
    <span><strong>时间: </strong>{article.created_at} </span>
  </div>
  <div class="post-abstract">
    {article.content}
  </div>
</div>
