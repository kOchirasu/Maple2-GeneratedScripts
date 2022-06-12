using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000208: Nick
/// </summary>
public class _11000208 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000892$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000894$
                // - There's been plenty of talk about Captain $npcName:11000044[gender:0]$'s leadership in Dark Wind, but I like his style. He said he'd evaluate every member based on their skill and performance. That's fair and reasonable.
                return 20;
            case (20, 1):
                // $script:0831180407000895$
                // - Those who have problems with it clearly just aren't good enough.
                return -1;
            case (30, 0):
                // $script:0831180407000896$
                // - Follow this road southward to find the Barrota Trading Company's warehouse at the end. Start your search there, and you should find $item:20000046$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
