for dir in /opt/sublime_text_3/Icon/*; do
    size="${dir##*/}"
    xdg-icon-resource install --novendor --size "${size/x*}" "$dir/sublime-text.png" "sublime-text"
done
gtk-update-icon-cache -f -t /usr/share/icons/hicolor > /dev/null 2>&1
