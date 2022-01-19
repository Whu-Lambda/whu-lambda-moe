<script>
  import ArticleCard from '$lib/components/ArticleCard.svelte';

  export let articles = [
    {
      id: 1,
      name: 'undefined',
      author: 'Whu Lambda',
      created_at: '2022-01-18',
      content: `undefined`
    }
  ];
</script>

<h4>近期文章</h4>

{#each articles as article, idx (idx)}
  <ArticleCard {article} />
{/each}
