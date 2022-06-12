using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001315: Amorro
/// </summary>
public class _11001315 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005034$
    // - It's a beautiful day, isn't it? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005691$
                // - People are always asking me if I'm okay living with my gramps. Well, I am!
                return 40;
            case (40, 1):
                // $script:1227194507005692$
                // - I don't care if you think he's a screaming old fart. If you ask me, he's a great man!
                switch (selection) {
                    // $script:1227194507005693$
                    // - Your grandpa isn't popular, is he?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227194507005694$
                // - They're just jealous of how great he is! Gramps talks loud so people can hear him clearly. Isn't that nice? 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
