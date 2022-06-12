using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001663: Ereve
/// </summary>
public class _11001663 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0617211107006373$
    // - Welcome, $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0617211107006374$
                // - You've grown strong, my hero. I look forward to hearing more great tales of your exploits.
                return -1;
            case (20, 0):
                // $script:0426085907008441$
                // - We hope our faith in you is well deserved.
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
