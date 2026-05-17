(function(){
  function ready(fn){
    if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',fn,{once:true});
    else fn();
  }

  ready(function(){
    const header=document.querySelector('header');
    const nav=header&&header.querySelector('nav');
    const menu=document.getElementById('main-menu');
    if(!header||!nav||!menu) return;
    if(menu.dataset.ocMobileInit==='true') return;
    menu.dataset.ocMobileInit='true';
    menu.classList.add('oc-mobile-drawer');

    const actions=[...nav.children].find(el=>el.classList&&el.classList.contains('flex')&&el.classList.contains('items-center')&&el.classList.contains('gap-4')) || nav.lastElementChild;
    const searchInput=document.getElementById('search-input');

    let overlay=document.querySelector('.oc-nav-overlay');
    if(!overlay){
      overlay=document.createElement('div');
      overlay.className='oc-nav-overlay';
      document.body.appendChild(overlay);
    }

    let mobileActions=nav.querySelector('.oc-mobile-actions');
    if(!mobileActions){
      mobileActions=document.createElement('div');
      mobileActions.className='oc-mobile-actions';

      const searchBtn=document.createElement('button');
      searchBtn.type='button';
      searchBtn.className='oc-mobile-search';
      searchBtn.setAttribute('aria-label','Open search');
      searchBtn.innerHTML='<span>⌕</span>';

      const navBtn=document.createElement('button');
      navBtn.type='button';
      navBtn.className='oc-nav-toggle';
      navBtn.setAttribute('aria-label','Open navigation');
      navBtn.setAttribute('aria-expanded','false');
      navBtn.innerHTML='<span>☰</span>';

      mobileActions.append(searchBtn,navBtn);
      if(actions) nav.insertBefore(mobileActions,actions);
      else nav.appendChild(mobileActions);
    }

    const searchBtn=mobileActions.querySelector('.oc-mobile-search');
    const navBtn=mobileActions.querySelector('.oc-nav-toggle');

    let searchRow=menu.querySelector('.oc-mobile-search-row');
    if(!searchRow){
      searchRow=document.createElement('div');
      searchRow.className='oc-mobile-search-row';
      searchRow.hidden=true;
      const mobileInput=document.createElement('input');
      mobileInput.type='search';
      mobileInput.placeholder='Search the site';
      searchRow.appendChild(mobileInput);
      menu.prepend(searchRow);
    }
    const mobileInput=searchRow.querySelector('input');

    let mobileApply=menu.querySelector('.oc-mobile-apply');
    if(!mobileApply){
      mobileApply=document.createElement('a');
      mobileApply.className='oc-mobile-apply';
      mobileApply.textContent='Apply Now';
      const existingApply=(actions&&actions.querySelector('a[href*="enquiry"]'))||document.querySelector('a[href*="enquiry"]');
      mobileApply.href=existingApply?existingApply.getAttribute('href'):'#';
      menu.prepend(mobileApply);
    }

    function closeMenus(){
      menu.classList.remove('oc-open');
      overlay.classList.remove('oc-open');
      navBtn.setAttribute('aria-expanded','false');
      menu.querySelectorAll('.menu-item.oc-expanded').forEach(item=>{
        item.classList.remove('oc-expanded');
        const btn=item.querySelector('[data-menu-toggle]');
        const panel=item.querySelector('[data-menu]');
        if(btn) btn.setAttribute('aria-expanded','false');
        if(panel) panel.classList.add('hidden');
      });
    }

    function openMenus(){
      menu.classList.add('oc-open');
      overlay.classList.add('oc-open');
      navBtn.setAttribute('aria-expanded','true');
    }

    navBtn.addEventListener('click',function(){
      if(window.innerWidth>900) return;
      if(menu.classList.contains('oc-open')) closeMenus();
      else openMenus();
    });

    overlay.addEventListener('click',closeMenus);
    document.addEventListener('keydown',function(e){ if(e.key==='Escape') closeMenus(); });
    window.addEventListener('resize',function(){ if(window.innerWidth>900){ closeMenus(); searchRow.hidden=true; } });

    if(searchBtn){
      searchBtn.addEventListener('click',function(){
        if(searchInput){
          searchInput.classList.toggle('hidden');
          if(!searchInput.classList.contains('hidden')) searchInput.focus();
          return;
        }
        searchRow.hidden=!searchRow.hidden;
        if(!searchRow.hidden && mobileInput) mobileInput.focus();
      });
    }

    if(mobileInput){
      mobileInput.addEventListener('keydown',function(e){
        if(e.key!=='Enter') return;
        const value=mobileInput.value.trim();
        if(!value) return;
        if(typeof window.find==='function') window.find(value);
      });
    }

    menu.querySelectorAll('.menu-item').forEach(function(item){
      const btn=item.querySelector('[data-menu-toggle]');
      const panel=item.querySelector('[data-menu]');
      if(!btn||!panel) return;
      btn.setAttribute('aria-expanded','false');
      btn.addEventListener('click',function(e){
        if(window.innerWidth>900) return;
        e.preventDefault();
        e.stopPropagation();
        const isOpen=item.classList.contains('oc-expanded');
        menu.querySelectorAll('.menu-item.oc-expanded').forEach(function(other){
          if(other===item) return;
          other.classList.remove('oc-expanded');
          const otherBtn=other.querySelector('[data-menu-toggle]');
          const otherPanel=other.querySelector('[data-menu]');
          if(otherBtn) otherBtn.setAttribute('aria-expanded','false');
          if(otherPanel) otherPanel.classList.add('hidden');
        });
        item.classList.toggle('oc-expanded',!isOpen);
        btn.setAttribute('aria-expanded',String(!isOpen));
        panel.classList.toggle('hidden',isOpen);
      });
    });

    menu.querySelectorAll('a').forEach(function(link){
      link.addEventListener('click',function(){ if(window.innerWidth<=900) closeMenus(); });
    });
  });
})();
