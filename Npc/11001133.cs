using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001133: Hujo
/// </summary>
public class _11001133 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003875$
    // - Do you have business with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003878$
                // - I'm trapped here! There are monsters everywhere. I knew this place was dangerous, but...
                switch (selection) {
                    // $script:0911192907003879$
                    // - Then why did you come here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0911192907003880$
                // - I have my reasons.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
