using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000365: Luchen
/// </summary>
public class _11000365 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001508$
    // - Shush! What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001510$
                // - Shush! Please leave quietly. I'm done for if they find out I'm here. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
