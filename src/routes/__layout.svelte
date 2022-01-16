<div class="container-fluid sticky-footer-wrapper">
  <header class="d-flex flex-wrap justify-content-center align-items-center py-2 mb-4 border-bottom">
    <a href="/" class="me-auto">
      <img
        class="logo"
        src="https://media.githubusercontent.com/media/Whu-Lambda/whu-lambda-moe/Nextjs/public/imgs/logo.png"
        alt="logo"
      />
    </a>

    <ul class="nav nav-pills">
      <li class="nav-item"><a href="/articles" class="nav-link">近期文章</a></li>
      <li class="nav-item"><a href="/events" class="nav-link">活动预告</a></li>
      <li class="nav-item"><a href="/about" class="nav-link">关于我们</a></li>
      <li class="nav-item"><a href="/member" class="nav-link">加入我们</a></li>
    </ul>
  </header>

  <main class="page-body">
    <slot />
  </main>

  <footer class="page-footer">
    <hr />

    <div class="d-flex justify-content-center my-3">
      <span>
        © 2022<a href="https://lookelooke.com">whu-lambda</a>
      </span>
      <span class="ms-3">
        <a target="_blank" href="https://beian.miit.gov.cn/">鄂ICP备20210xxxxx号-1</a>
      </span>
      <span class="ms-3">
        <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=42010602004616">
          <img class="d-inline me-1" src="/beiantubiao.png" alt="备案图标" />鄂公网安备4201060xxxxxxx号
        </a>
      </span>
    </div>
  </footer>
</div>

<style>
  /* Sticky footer(页脚沉底)
   * https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers
  */

  .sticky-footer-wrapper {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .page-footer {
    flex-shrink: 0;
  }

  .page-body {
    flex-grow: 1;
  }
  /* end sticky footer */

  a {
    text-decoration: none;
  }

  .logo {
    height: 2rem;
  }
</style>
