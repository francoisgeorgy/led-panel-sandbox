void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 position = ( fragCoord.xy / iResolution.xy );

    float color = 0.0;
    color += sin( position.x * cos( iTime / 15.0 ) * 80.0 ) + cos( position.y * cos( iTime / 15.0 ) * 10.0 );
    color += sin( position.y * sin( iTime / 10.0 ) * 40.0 ) + cos( position.x * sin( iTime / 25.0 ) * 40.0 );
    color += sin( position.x * sin( iTime / 5.0 ) * 10.0 ) + sin( position.y * sin( iTime / 35.0 ) * 80.0 );
    color *= sin( iTime / 10.0 ) * 0.5;

    fragColor = vec4( vec3( color, color * 0.5, sin( color + iTime / 3.0 ) * 0.75 ), 1.0 );
}
