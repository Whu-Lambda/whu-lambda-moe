<script>
  import Article from './Article.svelte';

  export let articles = [
    {
      id: 1,
      name: 'Recurring Period Optimized Using Number theory',
      about: 'CPP多线程和和数论优化计算循环长度',
      author: 'Mamiya Hasaki'
    },
    {
      id: 2,
      name: 'Rethinking Reactivity',
      about: 'React 和 Svelte 框架的实现思路和使用体验比较',
      author: 'Minakami Yuki'
    },
    {
      id: 3,
      name: 'Googology in Coq',
      about: 'Coq 公理化大数算术',
      author: 'oCau'
    },
    {
      id: 4,
      name: 'Undefinded Behaviours in C',
      about: 'C语言中未定义行为',
      author: 'KnifeFire'
    }
  ];
</script>

<div class="p-5">
  <h2># 文章</h2>
  <ol>
    {#each articles as article}
      <li><a href="/articles/1"><span class="h5">《{article.name}》</span> | {article.author}</a></li>
    {/each}
  </ol>
</div>

<style>
  h2 {
    color: green;
  }
  a{
      text-decoration: solid;
  }
</style>
