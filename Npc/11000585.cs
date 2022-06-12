using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000585: Seamus
/// </summary>
public class _11000585 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 40
    }

    // Select 0:
    // $script:0831180610000843$
    // - Ahoy!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610000844$
                // - Welcome to the $map:02000124$ cruise ship!
                return 1;
            case (1, 1):
                // $script:0831180610000845$
                // - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
                return 1;
            case (1, 2):
                // $script:0831180610000846$
                // - It's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison.
                //   Are you interested?
                return -1;
            case (40, 0):
                // $script:0831180610000850$
                // - Hey there! You looking for the cruise ship to $map:02000124$?
                switch (selection) {
                    // $script:0831180610000851$
                    // - Yep!
                    case 0:
                        return 41;
                    // $script:0831180610000852$
                    // - What is $map:02000124$?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180610000853$
                // - Hey, it's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison. 
                return 41;
            case (41, 1):
                // $script:0831180610000854$
                // - Looks like you're short on cash. Come on back when you've got it, because this tour is worth the money! You've never seen such suffering, such misery! It builds character.
                return -1;
            case (42, 0):
                // $script:0831180610000855$
                // - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.Next,
            (1, 1) => NpcTalkButton.Next,
            (1, 2) => NpcTalkButton.TakeBoat,
            _ => NpcTalkButton.None,
        };
    }
}
