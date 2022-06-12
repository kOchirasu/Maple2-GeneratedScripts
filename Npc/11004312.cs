using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004312: Veliche
/// </summary>
public class _11004312 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0928133807011350$
    // - The future is in our hands.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0928133807011351$
                // - We're on alien soil. Don't let your guard down.
                return -1;
            case (20, 0):
                // $script:0116153807012734$
                // - I have no missions for you right now.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
