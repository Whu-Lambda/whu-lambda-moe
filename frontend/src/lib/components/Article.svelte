<script>
  export let article;
</script>

<div >
  <h2>{article.name}</h2>
  <p class="text-center py-3"><span><strong>作者：</strong> {article.author}</span> | <span><strong>时间：</strong>{article.created_at}</span></p>
  <div class="mb-5">
    <img class="cover" src={article.cover} alt="封面" />
  </div>
  <p>{article.content}</p>
</div>

<style>
  .cover {
    max-width: 100%;
  }
</style>
