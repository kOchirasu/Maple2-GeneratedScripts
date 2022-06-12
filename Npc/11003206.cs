using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003206: Mark
/// </summary>
public class _11003206 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008235$
    // - If it weren't for you, those thugs would have got me. I owe you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008236$
                // - I'd be a goner if you hadn't shown up.
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
