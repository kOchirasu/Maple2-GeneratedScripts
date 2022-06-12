using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001431: Ruche
/// </summary>
public class _11001431 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005428$
    // - ...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005516$
                // - ...
                switch (selection) {
                    // $script:1222203907005517$
                    // - I heard you talk!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005518$
                // - <font color="#909090">($npcName:11001431[gender:0]$ tilts his head.)</font>
                switch (selection) {
                    // $script:1222203907005519$
                    // - Maybe I'm hearing things...
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1222203907005520$
                // - ...Heh.
                //   <font color="#909090">(Did $npcName:11001431[gender:0]$ just giggle...?)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
