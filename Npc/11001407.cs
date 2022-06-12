using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001407: Mian
/// </summary>
public class _11001407 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005404$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1230100207005748$
                // - ...
                switch (selection) {
                    // $script:1230100907005749$
                    // - What's with the quiet act?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1230100907005750$
                // - <font color="#909090">($npcName:11001407[gender:0]$ stares at you without saying a word.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
