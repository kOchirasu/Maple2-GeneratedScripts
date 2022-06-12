using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000352: Steve
/// </summary>
public class _11000352 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001463$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001466$
                // - You can't step on flowers like that! Don't lie to me, I saw you!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
