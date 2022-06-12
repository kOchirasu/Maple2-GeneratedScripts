using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001588: Rejan
/// </summary>
public class _11001588 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006076$
    // - I miss Calibre... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006127$
                // - Can we ever go back to Calibre Island?
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
