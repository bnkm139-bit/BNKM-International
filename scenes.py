"""Hand-authored SVG scene illustrations of the oil & gas industry.
Duotone / blueprint treatment to match the BNKM design system.
Each scene is a self-contained <svg>; gradient ids are namespaced per scene
so multiple scenes can coexist on one page without id collisions."""

# --------------------------------------------------------------------------
# REFINERY AT DUSK — distillation columns, storage tanks, spheres, flare stack
# --------------------------------------------------------------------------
REFINERY = '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Oil and gas refinery at dusk: distillation columns, storage tanks, LPG spheres and a lit flare stack">
 <defs>
  <linearGradient id="rfSky" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#06121F"/><stop offset=".65" stop-color="#102A40"/><stop offset="1" stop-color="#1A3A52"/>
  </linearGradient>
  <radialGradient id="rfGlow" cx=".52" cy="1" r=".75">
   <stop offset="0" stop-color="#1FB6A6" stop-opacity=".28"/><stop offset="1" stop-color="#1FB6A6" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="rfFlame" x1="0" y1="1" x2="0" y2="0">
   <stop offset="0" stop-color="#F0623A" stop-opacity="0"/><stop offset=".45" stop-color="#F0623A"/><stop offset="1" stop-color="#FFCE7A"/>
  </linearGradient>
  <radialGradient id="rfFlareGlow" cx=".5" cy=".5" r=".5">
   <stop offset="0" stop-color="#F0623A" stop-opacity=".55"/><stop offset="1" stop-color="#F0623A" stop-opacity="0"/>
  </radialGradient>
 </defs>
 <rect width="800" height="600" fill="url(#rfSky)"/>
 <ellipse cx="430" cy="470" rx="440" ry="170" fill="url(#rfGlow)"/>
 <g opacity=".55" fill="#0E2638"><circle cx="120" cy="90" r="1.3"/><circle cx="300" cy="60" r="1"/><circle cx="540" cy="80" r="1.2"/><circle cx="700" cy="50" r="1"/><circle cx="640" cy="120" r="1.1"/></g>

 <!-- far haze ridge -->
 <path d="M0 430 L120 415 L260 425 L420 408 L600 422 L800 410 L800 600 L0 600 Z" fill="#0C2236" opacity=".7"/>

 <!-- chimney + steam plume -->
 <g fill="#0F2638" stroke="#27506A" stroke-width="1">
  <rect x="262" y="205" width="16" height="255" rx="2"/>
 </g>
 <g fill="#9DB1C0" opacity=".10"><ellipse cx="276" cy="195" rx="18" ry="11"/><ellipse cx="292" cy="172" rx="24" ry="14"/><ellipse cx="312" cy="148" rx="30" ry="17"/><ellipse cx="338" cy="126" rx="34" ry="19"/></g>

 <!-- storage tanks (left) -->
 <g fill="#13283D" stroke="#27506A" stroke-width="1.2">
  <ellipse cx="98" cy="358" rx="62" ry="13"/><rect x="36" y="358" width="124" height="102"/><ellipse cx="98" cy="460" rx="62" ry="13" fill="#0E2034"/>
  <ellipse cx="210" cy="386" rx="46" ry="10"/><rect x="164" y="386" width="92" height="74"/>
 </g>
 <g stroke="#1FB6A6" stroke-width="1" opacity=".4"><line x1="36" y1="392" x2="160" y2="392"/><line x1="36" y1="426" x2="160" y2="426"/><line x1="164" y1="412" x2="256" y2="412"/></g>

 <!-- LPG spheres -->
 <g fill="#13283D" stroke="#27506A" stroke-width="1.2">
  <circle cx="582" cy="404" r="34"/><circle cx="648" cy="414" r="27"/>
  <g stroke="#1F4159" stroke-width="2"><line x1="560" y1="430" x2="556" y2="460"/><line x1="582" y1="438" x2="582" y2="460"/><line x1="604" y1="430" x2="608" y2="460"/><line x1="632" y1="436" x2="630" y2="460"/><line x1="664" y1="436" x2="666" y2="460"/></g>
 </g>
 <circle cx="572" cy="394" r="7" fill="#1FB6A6" opacity=".25"/>

 <!-- distillation columns (center) -->
 <g fill="#16314A" stroke="#2E5A74" stroke-width="1.2">
  <rect x="318" y="168" width="30" height="292" rx="6"/>
  <rect x="362" y="120" width="26" height="340" rx="6"/>
  <rect x="404" y="196" width="36" height="264" rx="6"/>
  <rect x="452" y="238" width="46" height="222" rx="5"/>
 </g>
 <!-- tray lines + platforms -->
 <g stroke="#0A1B2A" stroke-width="1" opacity=".8">
  <line x1="318" y1="210" x2="348" y2="210"/><line x1="318" y1="250" x2="348" y2="250"/><line x1="318" y1="290" x2="348" y2="290"/><line x1="318" y1="330" x2="348" y2="330"/><line x1="318" y1="370" x2="348" y2="370"/>
  <line x1="362" y1="170" x2="388" y2="170"/><line x1="362" y1="215" x2="388" y2="215"/><line x1="362" y1="260" x2="388" y2="260"/><line x1="362" y1="305" x2="388" y2="305"/><line x1="362" y1="350" x2="388" y2="350"/>
  <line x1="404" y1="240" x2="440" y2="240"/><line x1="404" y1="285" x2="440" y2="285"/><line x1="404" y1="330" x2="440" y2="330"/><line x1="404" y1="375" x2="440" y2="375"/>
 </g>
 <g fill="#0F2233" stroke="#2E5A74" stroke-width=".8">
  <rect x="310" y="246" width="46" height="6"/><rect x="356" y="206" width="38" height="6"/><rect x="396" y="300" width="52" height="6"/>
 </g>
 <!-- top vents -->
 <g stroke="#2E5A74" stroke-width="2" fill="none"><path d="M333 168 V150"/><path d="M375 120 V100"/><path d="M422 196 V180"/></g>
 <!-- handrail lights -->
 <g fill="#14D0BE" opacity=".7"><circle cx="333" cy="180" r="1.6"/><circle cx="375" cy="135" r="1.6"/><circle cx="422" cy="208" r="1.6"/><circle cx="475" cy="250" r="1.6"/></g>

 <!-- pipe rack -->
 <g stroke="#1F4159" stroke-width="2" fill="none"><line x1="250" y1="336" x2="540" y2="336"/><line x1="250" y1="346" x2="540" y2="346"/></g>
 <g stroke="#1FB6A6" stroke-width="1.2" opacity=".45" fill="none"><line x1="250" y1="341" x2="540" y2="341"/></g>
 <g stroke="#1F4159" stroke-width="3"><line x1="272" y1="336" x2="272" y2="380"/><line x1="332" y1="336" x2="332" y2="380"/><line x1="392" y1="336" x2="392" y2="380"/><line x1="452" y1="336" x2="452" y2="380"/><line x1="512" y1="336" x2="512" y2="380"/></g>

 <!-- flare stack (right) -->
 <circle cx="724" cy="138" r="60" fill="url(#rfFlareGlow)"/>
 <rect x="719" y="160" width="9" height="300" fill="#13283D" stroke="#27506A" stroke-width="1"/>
 <g stroke="#27506A" stroke-width="1" fill="none" opacity=".8"><path d="M719 220 l-14 8 M728 220 l14 8 M719 280 l-14 8 M728 280 l14 8 M719 340 l-14 8 M728 340 l14 8"/></g>
 <path d="M723 160 C708 138 736 130 726 108 C744 124 742 150 740 160 C736 150 730 150 723 160 Z" fill="url(#rfFlame)"/>
 <g fill="#FFCE7A" opacity=".8"><circle cx="730" cy="100" r="2"/><circle cx="716" cy="118" r="1.5"/></g>

 <!-- foreground ground + pipeline -->
 <rect x="0" y="460" width="800" height="140" fill="#081523"/>
 <g stroke="#1F4159" stroke-width="3" fill="none"><path d="M0 512 H300 q14 0 14 14 V560"/><path d="M380 560 V524 q0-14 14-14 H800"/></g>
 <g stroke="#1FB6A6" stroke-width="1" opacity=".35" fill="none"><path d="M0 512 H300"/><path d="M394 510 H800"/></g>
</svg>'''

# --------------------------------------------------------------------------
# OFFSHORE PLATFORM — jacket, deck modules, derrick, flare boom, supply vessel
# --------------------------------------------------------------------------
OFFSHORE = '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Offshore oil and gas platform at sea with derrick, deck modules, a lit flare boom and a supply vessel">
 <defs>
  <linearGradient id="ofSky" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#06121F"/><stop offset=".7" stop-color="#11304A"/><stop offset="1" stop-color="#1C4360"/>
  </linearGradient>
  <linearGradient id="ofSea" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#13344C"/><stop offset="1" stop-color="#071623"/>
  </linearGradient>
  <radialGradient id="ofSun" cx=".5" cy=".5" r=".5">
   <stop offset="0" stop-color="#F0A85A" stop-opacity=".5"/><stop offset="1" stop-color="#F0A85A" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="ofFlame" x1="0" y1="1" x2="0" y2="0">
   <stop offset="0" stop-color="#F0623A" stop-opacity="0"/><stop offset=".5" stop-color="#F0623A"/><stop offset="1" stop-color="#FFCE7A"/>
  </linearGradient>
  <radialGradient id="ofFlareGlow" cx=".5" cy=".5" r=".5">
   <stop offset="0" stop-color="#F0623A" stop-opacity=".5"/><stop offset="1" stop-color="#F0623A" stop-opacity="0"/>
  </radialGradient>
 </defs>
 <rect width="800" height="600" fill="url(#ofSky)"/>
 <ellipse cx="430" cy="380" rx="260" ry="120" fill="url(#ofSun)"/>
 <g opacity=".5" fill="#0E2638"><circle cx="120" cy="80" r="1.2"/><circle cx="650" cy="70" r="1"/><circle cx="540" cy="120" r="1.1"/></g>
 <!-- gulls -->
 <g stroke="#1FB6A6" stroke-width="1.4" fill="none" opacity=".5"><path d="M150 130 q8 -7 16 0 q8 -7 16 0"/><path d="M210 110 q6 -5 12 0 q6 -5 12 0"/></g>

 <!-- sea -->
 <rect x="0" y="382" width="800" height="218" fill="url(#ofSea)"/>
 <line x1="0" y1="382" x2="800" y2="382" stroke="#1FB6A6" stroke-width="1" opacity=".35"/>
 <g stroke="#1FB6A6" stroke-width="1" opacity=".12"><line x1="0" y1="410" x2="800" y2="410"/><line x1="0" y1="442" x2="800" y2="442"/><line x1="0" y1="478" x2="800" y2="478"/><line x1="0" y1="520" x2="800" y2="520"/><line x1="0" y1="566" x2="800" y2="566"/></g>
 <g fill="#F0A85A" opacity=".18"><rect x="412" y="386" width="14" height="180"/></g>

 <!-- platform -->
 <g stroke="#27506A" stroke-width="2" fill="none">
  <path d="M308 300 L286 560"/><path d="M352 300 L344 560"/><path d="M488 300 L500 560"/><path d="M532 300 L552 560"/>
  <path d="M300 360 L356 372 M488 372 L548 360 M315 430 L350 440 M492 440 L540 430 M308 500 L348 510 M495 510 L548 500"/>
  <path d="M356 372 L488 372 M350 440 L492 440 M348 510 L495 510" opacity=".7"/>
 </g>
 <!-- deck -->
 <rect x="292" y="286" width="256" height="20" fill="#16314A" stroke="#2E5A74" stroke-width="1"/>
 <!-- modules -->
 <g fill="#13283D" stroke="#2E5A74" stroke-width="1">
  <rect x="300" y="244" width="78" height="42" rx="2"/>
  <rect x="386" y="256" width="92" height="30" rx="2"/>
 </g>
 <!-- helideck -->
 <g><ellipse cx="339" cy="240" rx="34" ry="9" fill="#0F2436" stroke="#2E5A74" stroke-width="1"/><text x="333" y="244" font-family="monospace" font-size="11" fill="#1FB6A6">H</text></g>
 <!-- module windows -->
 <g fill="#14D0BE" opacity=".7"><circle cx="312" cy="268" r="1.6"/><circle cx="324" cy="268" r="1.6"/><circle cx="336" cy="268" r="1.6"/><circle cx="400" cy="270" r="1.6"/><circle cx="414" cy="270" r="1.6"/></g>
 <!-- derrick -->
 <g stroke="#2E5A74" stroke-width="1.6" fill="none">
  <path d="M470 256 L492 150 L514 256"/>
  <path d="M476 226 L508 226 M480 196 L504 196 M484 168 L500 168"/>
  <path d="M470 256 L508 226 M514 256 L476 226 M476 226 L504 196 M508 226 L480 196"/>
 </g>
 <circle cx="492" cy="148" r="2.4" fill="#FFCE7A"/>
 <!-- crane -->
 <g stroke="#2E5A74" stroke-width="2" fill="none"><path d="M360 256 L300 196"/><path d="M300 196 L300 230"/></g>
 <!-- flare boom + flame -->
 <circle cx="690" cy="176" r="48" fill="url(#ofFlareGlow)"/>
 <g stroke="#27506A" stroke-width="2" fill="none"><path d="M548 300 L690 184"/><path d="M556 318 L686 204"/><path d="M576 300 L600 290 M620 286 L644 276 M664 256 L686 240" opacity=".7"/></g>
 <path d="M688 184 C676 166 698 158 690 140 C704 154 702 176 700 184 C696 176 692 176 688 184 Z" fill="url(#ofFlame)"/>

 <!-- supply vessel -->
 <g fill="#0F2436" stroke="#2E5A74" stroke-width="1">
  <path d="M96 470 L226 470 L214 492 L108 492 Z"/>
  <rect x="180" y="448" width="40" height="22" rx="2"/>
 </g>
 <g stroke="#2E5A74" stroke-width="1.4" fill="none"><path d="M120 470 L120 446 L150 470"/></g>
 <g fill="#14D0BE" opacity=".8"><circle cx="190" cy="458" r="1.6"/><circle cx="206" cy="458" r="1.6"/></g>
 <g fill="#F0A85A" opacity=".15"><rect x="150" y="492" width="6" height="50"/></g>
</svg>'''

# --------------------------------------------------------------------------
# ONSHORE UPSTREAM — pump jacks (nodding donkeys), wellheads, tank, pipeline
# --------------------------------------------------------------------------
def _pumpjack(tx, ty, s, flip=False):
    f = "-1" if flip else "1"
    return f'''<g transform="translate({tx} {ty}) scale({s})">
  <g transform="scale({f} 1)">
   <!-- skid -->
   <rect x="-66" y="-8" width="132" height="10" fill="#0E2436" stroke="#2E5A74" stroke-width="1"/>
   <!-- prime mover / gearbox -->
   <rect x="34" y="-30" width="30" height="22" fill="#13283D" stroke="#2E5A74" stroke-width="1"/>
   <!-- samson post (A-frame) -->
   <path d="M-6 -8 L4 -96 L18 -8 Z" fill="#13283D" stroke="#2E5A74" stroke-width="1.4"/>
   <path d="M-2 -50 L14 -50" stroke="#2E5A74" stroke-width="1.4"/>
   <!-- walking beam -->
   <path d="M-78 -88 L52 -100 L52 -90 L-78 -78 Z" fill="#16314A" stroke="#2E5A74" stroke-width="1.4"/>
   <!-- counterweight + crank -->
   <circle cx="50" cy="-46" r="18" fill="#13283D" stroke="#2E5A74" stroke-width="1.4"/>
   <line x1="50" y1="-95" x2="50" y2="-64" stroke="#2E5A74" stroke-width="2.4"/>
   <!-- horse head + bridle -->
   <path d="M-78 -84 C-92 -84 -94 -70 -90 -58 L-78 -64 Z" fill="#16314A" stroke="#2E5A74" stroke-width="1.4"/>
   <line x1="-90" y1="-58" x2="-86" y2="-8" stroke="#2E5A74" stroke-width="1.4"/>
   <line x1="-83" y1="-58" x2="-80" y2="-8" stroke="#2E5A74" stroke-width="1.4"/>
   <!-- wellhead -->
   <rect x="-92" y="-22" width="14" height="22" fill="#0F2436" stroke="#2E5A74" stroke-width="1"/>
   <circle cx="4" cy="-96" r="2.4" fill="#14D0BE"/>
  </g>
 </g>'''

ONSHORE = f'''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Onshore oil field at dusk with pump jacks, a wellhead, a storage tank and a pipeline">
 <defs>
  <linearGradient id="onSky" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#07131F"/><stop offset=".6" stop-color="#102A40"/><stop offset="1" stop-color="#27475C"/>
  </linearGradient>
  <radialGradient id="onSun" cx=".5" cy=".5" r=".5">
   <stop offset="0" stop-color="#F4B66B" stop-opacity=".9"/><stop offset=".4" stop-color="#F0A85A" stop-opacity=".4"/><stop offset="1" stop-color="#F0A85A" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="onGround" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#0E2334"/><stop offset="1" stop-color="#070F19"/>
  </linearGradient>
 </defs>
 <rect width="800" height="600" fill="url(#onSky)"/>
 <ellipse cx="612" cy="392" rx="180" ry="140" fill="url(#onSun)"/>
 <circle cx="612" cy="392" r="42" fill="#F6C079" opacity=".85"/>
 <g opacity=".5" fill="#13314A"><circle cx="120" cy="70" r="1.2"/><circle cx="260" cy="50" r="1"/><circle cx="430" cy="90" r="1.1"/></g>
 <!-- distant ridge -->
 <path d="M0 398 L160 384 L340 396 L520 380 L700 394 L800 384 L800 600 L0 600 Z" fill="#0C2030" opacity=".8"/>
 <!-- ground -->
 <rect x="0" y="404" width="800" height="196" fill="url(#onGround)"/>
 <path d="M0 470 Q200 452 420 472 T800 466 V600 H0 Z" fill="#0A1A28" opacity=".6"/>
 <!-- pipeline -->
 <g stroke="#1F4159" stroke-width="4" fill="none"><path d="M0 520 H470 q16 0 16 -16 V470"/></g>
 <g stroke="#1FB6A6" stroke-width="1" opacity=".3" fill="none"><path d="M0 520 H470"/></g>
 <!-- storage tank (left) -->
 <g fill="#13283D" stroke="#27506A" stroke-width="1.2"><ellipse cx="92" cy="430" rx="48" ry="11"/><rect x="44" y="430" width="96" height="78"/></g>
 <line x1="44" y1="466" x2="140" y2="466" stroke="#1FB6A6" stroke-width="1" opacity=".4"/>
 {_pumpjack(300, 470, 1.0)}
 {_pumpjack(520, 484, 0.78)}
 {_pumpjack(690, 458, 1.18, flip=True)}
</svg>'''


def FIG(scene, alt_label):
    """Scene used as the figure in a split section (sits in the 4:3 panel)."""
    return (f'<div class="split-figure photo" role="img" aria-label="{alt_label}">'
            f'{scene}<span class="photo-tag">FIG &middot; site illustration</span></div>')


def BAND(scene, eyebrow, title):
    """Full-bleed image band with an overlaid caption."""
    return f'''<section class="imgband reveal" aria-label="{title}">
  {scene}
  <div class="cap">
    <p class="eyebrow">{eyebrow}</p>
    <h3>{title}</h3>
  </div>
</section>'''
