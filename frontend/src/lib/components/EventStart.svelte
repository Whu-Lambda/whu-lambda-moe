<script>
  export let events = [
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
  <h2># 分享</h2>
  <div class="py-4">
    <img class="img-fluid rounded" src="https://www.whu.edu.cn/images/2022010501.jpg" alt="cover" />
  </div>
  <div>
    <ol>
      {#each events as event}
        <li><span class="h5">{event.name}</span> | {event.author}</li>
      {/each}
    </ol>
    <a href="/events/1">>>详情</a>
  </div>
</div>

<style>
  h2 {
    color: red;
  }
  .cover {
    max-width: 100%;
  }
</style>
