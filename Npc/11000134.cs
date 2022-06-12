using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000134: Wolf Heart
/// </summary>
public class _11000134 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000557$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000558$
                // - Once a year, the Murpagoth warriors go on a pilgrimage through the Vayar Mountains. By the time they return, they've grown much stronger than they were before.
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
