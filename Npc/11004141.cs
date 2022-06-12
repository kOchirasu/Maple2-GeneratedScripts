using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004141: Kaitlyn
/// </summary>
public class _11004141 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010553$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010554$
                // - I wish he wore glasses. He's so intelligent and sensitive... It would be perfect... 
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
