(function(){
  const toggles = document.querySelectorAll('[data-menu-toggle]');
  const menus = document.querySelectorAll('[data-menu]');
  function closeAll(){ menus.forEach(m=>m.classList.add('hidden')); }
  toggles.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
      e.preventDefault();
      const key = btn.getAttribute('data-menu-toggle');
      const menu = document.querySelector('[data-menu="'+key+'"]');
      if(!menu) return;
      const willOpen = menu.classList.contains('hidden');
      closeAll();
      if(willOpen) menu.classList.remove('hidden');
    });
  });
  document.addEventListener('click',(e)=>{
    if(!e.target.closest('.menu-item')) closeAll();
  });
  document.addEventListener('keydown',(e)=>{ if(e.key==='Escape') closeAll(); });

  const searchToggle=document.getElementById('search-toggle');
  const searchInput=document.getElementById('search-input');
  if(searchToggle && searchInput){
    searchToggle.addEventListener('click',()=>{
      searchInput.classList.toggle('hidden');
      if(!searchInput.classList.contains('hidden')) searchInput.focus();
    });
  }
})();
