/* It can be hard manipulate the definition and drawing of strings in shaders, it often
   relies on arrays of numbers that are tidious to update manually and are pretty
   obfuscated compared to the original text.

   This shader tries to provide an easier framework for string manipulation where you
   can simply declare a string like this:

       makeStr(printHello) _H _e _l _l _o  __  _w _o _r _l _d    _end

   And directly use it in any function (More info in the "Common" tab):

       finalCol += printHello(uv);
*/

// String declarations
makeStr(printStr1)      _E _a _s _y __ _w _a _y __ _t _o __ _p _r _i _n _t __ _t _e _x _t __  _i _n __ _S _h _a _d _e _r _s _EXC _end
makeStr(printNum)       _P _r _i _n _t __ _S _t _a _t _i _c __ _D _i _g _i _t _s __ _2 _0 _2 _3                                  _end
makeStr1i(printDynNum)  _A _n _d __ _D _y _n _a _m _i _c __ _D _i _g _i _t _s __ _dig(i)                                         _end
makeStr1f(printDecNum)  _D _e _c _i _m _a _l __ _N _u _m _b _e _r _s __ _T _o _o __ _dec(i, 3)                                   _end
makeStr2f(printDynChar) _S _u _p _p _o _r _t _s __ _D _y _n _a _m _i _c __ _C _h _a _r _a _c _t _e _r _s __ _ch(i) __ _ch(j)     _end
makeStr(printSpecial)   _A _n _d __ _e _v _e _n __ _S _p _e _c _i _a _l __ _C _h _a _r _s __ _EXC _NUM _MUL _DIV _AT _UND        _end

makeStr(printLong)      _W _o _r _k _s __ _f _o _r __ _a _l _l __ _t _e _x _t __ _s _i _z _e _s
                        _COM __ _e _v _e _n __ _t _h _e __ _l _o _n _g _e _r __ _o _n _e _s __
                        _i _f __ _y _o _u __ _s _c _a _l _e __ _t _h _e __ _u _v _s _EXC                                         _end

// Color declarations
#define RED     vec3( 1,.3,.4)
#define GREEN   vec3(.2, 1,.4)
#define BLUE    vec3(.2,.8, 1)
#define RAINBOW abs(cos(uv.x + vec3(5,6,1)))

void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    // Normalized uv coordinates
    vec2 uv = fragCoord / iResolution.y;

    // Final color
    vec3 col = vec3(0);

    // Font Size (higher values = smaller font)
    const float font_size = 9.;

    uv *= font_size;        // Scale font with font_size
    uv.y -= font_size - 1.; // Start drawing from the top


    col += RED * printStr1(uv);                       // "Easy way to print text in shaders"
    uv.y += 2.; // Move the cursor down

    col += GREEN * printNum(uv);                      // "Static Digits"
    uv.y++;

    col += GREEN/.6 * printDynNum(uv, int(iTime)%10); // "Dynamic Digits"
    uv.y++;

    col += GREEN/.4 * printDecNum(uv, iTime);         // "Decimal Numbers"
    uv.y+=2.;

    col += BLUE * printDynChar(uv, mod(iTime, 26.), mod(iTime*2., 26.)); // "Dynamic Characters"
    uv.y++;

    col += RAINBOW  * printSpecial(uv);                // "Special Characters"
    uv.y+=.7;

    uv *= 2.; // Multiply uv by 2 to make it smaller

    col += printLong(uv);                              // "Works for all text sizes..."

    fragColor = vec4(col, 1.);
}
