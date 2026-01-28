{
  stdenv,
  fetchFromGitHub,
  fetchzip,
  gnused,
  jre,
}:

stdenv.mkDerivation rec {
  name = "pepper";
  version = "2023.05.15";

  src = fetchzip {
    url = "https://korpling.german.hu-berlin.de/saltnpepper/pepper/download/stable/Pepper_${version}.zip";
    stripRoot = false;
    hash = "sha256-Clqg7jbKVyy0cQRmCPWSSuLsodg9IiyhPvS0JwCE+G8=";
  };

  installPhase = ''
    runHook preInstall

    mkdir -p $out/share/pepper $out/bin
    cp -r ./. $out/share/pepper/

    ln -s $out/share/pepper/pepper.sh $out/bin/pepper

    runHook postInstall
  '';

  postFixup = ''
    ${gnused}/bin/sed -i "s|-classpath lib/\*:plugins/\*|-classpath $out/share/pepper/lib/\*:$out/share/pepper/plugins/\*|" $out/share/pepper/pepper.sh $out/share/pepper/pepperStart.sh $out/share/pepper/pepper-debug.sh
    ${gnused}/bin/sed -i "s|java|PEPPER_HOME=$out/share/pepper ${jre}/bin/java|" $out/share/pepper/pepper.sh $out/share/pepper/pepperStart.sh $out/share/pepper/pepper-debug.sh
    ${gnused}/bin/sed -i "s|./conf/logback.xml|$out/share/pepper/conf/logback.xml|" $out/share/pepper/pepper.sh $out/share/pepper/pepperStart.sh $out/share/pepper/pepper-debug.sh
    ${gnused}/bin/sed -i "s|./plugins/|$out/share/pepper/plugins/|" $out/share/pepper/conf/pepper.properties 
  '';
}
