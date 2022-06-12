using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000099: Caprio
/// </summary>
public class _11000099 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000388$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000391$
                // - Hey, $MyPCName$! Have you heard about the hero who collected over 1,000 mesos just by hunting monsters? That's me!
                return 30;
            case (30, 1):
                // $script:0831180407000392$
                // - I think I was born to be a hunter. You should find something that you can be good at and have fun doing.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
