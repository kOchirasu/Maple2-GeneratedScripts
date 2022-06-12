using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004207: Koomkoom
/// </summary>
public class _11004207 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0803202415009087$
    // - Heheh, want to play with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0803202415009088$
                // - Heheheh... I've got something real fun cooked up for those humans. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
