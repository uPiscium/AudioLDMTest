{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
    {
      devShells.x86_64-linux.default = pkgs.mkShell {
        packages = with pkgs; [
          openssl
          llvm_14
        ];
        buildInputs = with pkgs; [
          openssl
          llvm_14
        ];
        LD_LIBRARY_PATH = "${pkgs.openssl}/lib:${pkgs.llvm_14}/lib";
        PKG_CONFIG_PATH = "${pkgs.openssl.dev}/lib/pkgconfig";
      };
    };
}

