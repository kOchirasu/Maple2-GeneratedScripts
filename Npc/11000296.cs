using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000296: Jasper
/// </summary>
public class _11000296 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001177$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001180$
                // - Oh! I's so happy to see another human being here!
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
