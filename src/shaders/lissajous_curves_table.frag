// Overlay

vec3 palette( in float k, in vec3 a, in vec3 b, in vec3 c, in vec3 d ) {
    return a + b*cos( 6.28318*(c*k+d) );
}

void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    fragColor = texture(iChannel0, fragCoord/iResolution.xy);
    if (iMouse.z > 0.5) return;

    vec2 uv = (fragCoord.xy)/iResolution.y;
    vec2 fuv = fract(uv*7.)-.5;
    vec2 fid = floor(uv*7.);
    vec2 id0 = fid;

    if (fid.x+fid.y == 0.) return;
    if (fid.x*fid.y == 0.) fid = vec2(max(fid.x, fid.y));

    vec2 p = vec2( cos(iTime*.2 * fid.x), sin(iTime*.2 * fid.y) )*.45;

    // lines overlay
    float d = 0.;
    if (id0.y > 0.) d += smoothstep(.03, .0, abs(fuv.y - p.y)); // horizontal
    if (id0.x > 0.) d += smoothstep(.03, .0, abs(fuv.x - p.x)); // vertical

    float intensity = smoothstep(-1., 1., sin(iTime*.35)*8.)*.75;
    fragColor.rgb += vec3(d)*intensity;

    // dots overlay
    vec3 color = palette((fid.x+fid.y)/14., vec3(.75), vec3(0.5), vec3(1.), vec3(0., .25, .5));
    fragColor.rgb = mix(fragColor.rgb, color+.4, smoothstep(.06, .04, length(fuv - p)) );
}