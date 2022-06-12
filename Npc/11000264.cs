using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000264: Ladin
/// </summary>
public class _11000264 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407001077$
    // - Need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001080$
                // - After the Blue Lapenta broke, top scholars from across the world descended on the $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
                return -1;
            case (40, 0):
                // $script:0831180407001081$
                // - Can't you see I'm trying to focus?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
