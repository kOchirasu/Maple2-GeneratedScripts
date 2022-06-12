using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004154: Unita
/// </summary>
public class _11004154 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010579$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010580$
                // - Wow, just look at that ocean! This place is so different from $map:02000051$. It really is nice to get out and explore the world once in a while.
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
