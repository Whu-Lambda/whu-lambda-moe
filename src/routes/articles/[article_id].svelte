<script>
  import Article from '$lib/components/Article.svelte';

  export let article = {
    id: 1,
    name: 'undefined',
    author: 'Whu Lambda',
    created_at: '2022-01-18',
    cover: '/logo.png',
    content: `undefined`
  };
</script>

<Article {article} />
