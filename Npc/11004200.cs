using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004200: Mrs. Ibelin
/// </summary>
public class _11004200 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010648$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010649$
                // - My son is always thinking of me, and it makes me so very happy. He's such a good boy! I don't know how I'd get along without him.
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
