using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003199: Joddy
/// </summary>
public class _11003199 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008226$
    // - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008227$
                // - A fight between siblings can be even more fearsome than a duel between sworn enemies. I wouldn't stand a chance if $npcName:11000069[gender:1]$ were my sister.
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
