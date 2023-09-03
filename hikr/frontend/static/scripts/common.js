$(document).ready(function () {
  const header = $('header');
  const footer = $('footer');

  header.html(`
    <div class="px-6 sm:px-4 xl:px-4 border-b border-solid border-gray2 flex flex-col">
    <div class="transition-all ease-linear duration-300 d3hxo23 overflow-hidden sm:overflow-visible">
      <div class="flex flex-row items-center justify-between du3dmzv">
        <div class="block sm:hidden xmedia"></div>
        <div class="flex flex-row items-center space-x-10"><a href="/" class="lg:pl-6"
            aria-label="Hikr logo" data-event-label="Hikr logo"><img src="../static/images/logo.png" alt="Hikr logo"
              height="3"></a>
          <div class="m1t1fice hidden gl:block xmedia">
            <form id="search-form" class="outline-none w-full">
              <div class="flex flex-row -space-x-0.5">
                <div class="w-full hover:z-20 de68ah0">
                  <div class="relative">
                    <div class="absolute top-2.5 left-2.5" style="width: 22px; height: 22px;" data-icon-c="icon-110">
                    </div><input id="keyword-bar-in-search" type="search" name="keywords" placeholder="Search events"
                      aria-label="Search events"
                      class="appearance-none border p-2 pl-4 border-gray3 outline-none hover:border-gray6 focus:border-viridian hover:z-10 focus:z-10 iofyh9x lg:min-w-[120px] xl:min-w-[300px] rounded-l-lg flex-grow w-full rounded-r-none placeholder:text-gray6"
                      data-element-name="keyword-bar-in-search" data-event-label="Keyword search" value="">
                  </div>
                </div>
                <div class="transition-all ease-out duration-200 opacity-1 flex-[1_0_50%]">
                  <div class="flex flex-row -space-x-0.5">
                    <button id="location-search-submit" data-testid="location-search-submit"
                      class="relative rounded-r-lg p-2 flex flex-col items-center justify-center bqsnhz9" style="background-color: #26a269;"
                      aria-label="Search events" data-event-label="Search submit" type="submit">
                      <div id="search-button" style="width: 20px; height: 20px;">
                        <!-- search icon -->
                        <i class="fa-solid fa-magnifying-glass" style="color: whitesmoke;"></i>

                      </div>
                    </button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="block sm:hidden xmedia"></div>
        <div class="sm:ml-4 hidden sm:block xmedia">
          <div class="flex flex-row space-x-5 items-center">
            <div class="gl:hidden hidden sm:block xmedia"></div>
            <a id="login-link" data-element-name="header-loginLink" data-event-label="Log in"
              class="ds-font-small-medium hover:no-underline text-gray7 hover:text-viridian" href="/login/">Log
              in</a><a id="register-link"
              class="ds-font-small-medium hover:no-underline text-gray7 hover:text-viridian s2x9qzh whitespace-nowrap justify-center"
              data-element-name="header-registerLink" data-event-label="Sign up" href="/sign-up/">Sign
              up</a>
          </div>
        </div>
      </div>
      <div class="mt-1 mb-2 pointer-events-none block gl:hidden xmedia"></div>
    </div>
  </div>`);

  footer.html(`
    <div class="px-6 sm:px-4 xl:px-0 md:max-w-screen my-0 mx-auto flex flex-col space-y-6 pb-4">
  <div class="flex flex-col sm:flex-row justify-between">
    <div class="w-1/3 mb-3">
      <h2>Your Account</h2>
      <ul>
        <li class="my-1"><a href="/sign-up/" data-element-name="footer-signUp" data-event-label="Sign up variant"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">Sign up</a>
        </li>
        <li class="my-1"><a href="/login/" data-element-name="footer-logIn" data-event-label="Log in"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">Log in</a>
        </li>
      </ul>
    </div>
    <div class="w-1/3 mb-3">
      <h2>Discover</h2>
      <ul>
        <li class="my-1"><a href="/groups/" data-element-name="footer-groups" data-event-label="Groups"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">Groups</a>
        </li>

        <li class="my-1"><a href="/events/" data-element-name="eventsFooterLink" data-event-label="Events"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">Events</a>
        </li>
      </ul>
    </div>
    <div class="w-1/3 mb-3">
      <h2>Hikr</h2>
      <ul>
        <li class="my-1"><a href="/" data-element-name="footer-about" data-event-label="About"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">About</a></li>
        <li class="my-1"><a href="/" data-element-name="footer-blog" data-event-label="Blog"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer">Blog</a></li>
      </ul>
    </div>
    <div class="w-1/3 mb-3">
      <h2>Follow Us</h2>
      <ul>
        <li class="my-1"><a href="https://www.github.com/evanceodoyo/hikr" data-element-name="follow-us"
            data-event-label="FollowUs"
            class="ds-font-small hover:no-underline text-gray4 hover:text-white cursor-pointer"><i
              class="fa-brands fa-github fa-xl"></i></a></a></li>
      </ul>
    </div>
  </div>

  <div class="flex justify-center items-center">
    <span class="text-white">© 2023 Hikr</span>
  </div>

</div>`);
});