import QtQuick 2.0
import Sailfish.Silica 1.0
import "functions.js" as F

Page {

    property string uid
    property alias name: userName.text
    property alias icon: userIcon.source

    signal switchToBadges();

    SilicaFlickable {
        anchors.fill: parent;

        Column {
            width: parent.width

            PageHeader {
                title: qsTr("Friend Detail")
            }

            Row {
                anchors {
                    left: parent.left
                    right: parent.right
                    margins: Theme.paddingMedium
                }
                spacing: Theme.paddingMedium
                Image {
                    width: 86;
                    height: 86;

                    id: userIcon
                }
                Label {
                    id: userName
                }
            }

            BackgroundItem {
                width: parent.width;
                Label {
                    anchors {
                        verticalCenter: parent.verticalCenter
                        left: parent.left
                        right: parent.right
                        margins: Theme.paddingMedium
                    }
                    text: qsTr("Badges")
                }
                onClicked: {
                    switchToBadges()
                }
            }


        }
    }
}
