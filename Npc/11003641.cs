using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003641: Ain
/// </summary>
public class _11003641 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009124$
    // - Hey hey hey!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009125$
                // - You here to jam, my friend? Let your inner songbird free!
                switch (selection) {
                    // $script:1109121007009126$
                    // - ♬There's someone that I seek! And I don't have all week! ♬
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009127$
                // - Ow ow ow, my ears! Did someone hit your songbird with a hammer?
                switch (selection) {
                    // $script:1109121007009128$
                    // - I... I think I'm gonna cry...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009129$
                // - Don't be like that, $male:man,female:lady$. Here, I know something what'll cheer you right up.
                switch (selection) {
                    // $script:1109121007009130$
                    // - Oh?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009131$
                // - I've got a message for our fabulous friend, $npcName:11003535[gender:1]$. "The unbreakable link between heart and song!"
                switch (selection) {
                    // $script:1109121007009132$
                    // - Okay...
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009133$
                // - Cheer up. You probably just had a frog in your throat, friend.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
