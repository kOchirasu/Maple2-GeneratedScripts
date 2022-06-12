using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000266: Jin
/// </summary>
public class _11000266 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001085$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001087$
                // - Captain $npcName:11000044[gender:0]$ commands Dark Wind now, but before the Blue Lapenta broke we were led by Winn Stilton. Every member of Dark Wind, myself included, considered Captain Stilton a true hero.
                return 20;
            case (20, 1):
                // $script:0831180407001088$
                // - That's why we can never forgive $npcName:11000064[gender:0]$! He not only destroyed the Blue Lapenta, but he also killed Captain Stilton!
                return -1;
            case (30, 0):
                // $script:0831180407001089$
                // - I can't believe $npcName:11000044[gender:0]$ ended Captain Stilton's life. That brazen coward fooled us all!
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
