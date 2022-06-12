using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000173: Ralph
/// </summary>
public class _11000173 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000723$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000726$
                // - Everyone acts as if they're the purest, noblest people in the world, but on the inside, we're all equally rotten. Hey, $MyPCName$! Live your life the way you want. Don't let anyone tell you what to do!
                return -1;
            case (40, 0):
                // $script:0831180407000727$
                // - Your youthful recklessness will be your undoing. Search $map:02000141$ if you can. I very much doubt you'll return alive. 
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
