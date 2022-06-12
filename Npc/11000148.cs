using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000148: Cavan
/// </summary>
public class _11000148 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000631$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000634$
                // - If I wasn't charged with $map:63000004$, I could've joined the delegation. I hate that no one else can fill in for me! 
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
