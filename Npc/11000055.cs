using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000055: Joseph
/// </summary>
public class _11000055 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000237$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000240$
                // - $MyPCName$, if you're hungry you should come inside. This is my house right here, and my mom is baking cookies.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
