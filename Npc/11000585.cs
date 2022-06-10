using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000585: Seamus
/// </summary>
public class _11000585 : NpcScript {
    internal _11000585(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000843$ 
                // - Ahoy!
                return true;
            case 1:
                // $script:0831180610000844$ 
                // - Welcome to the $map:02000124$ cruise ship!
                // $script:0831180610000845$ 
                // - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
                // $script:0831180610000846$ 
                // - It's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison.
                //   Are you interested?
                return true;
            case 40:
                // $script:0831180610000850$ 
                // - Hey there! You looking for the cruise ship to $map:02000124$?
                switch (selection) {
                    // $script:0831180610000851$
                    // - Yep!
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180610000852$
                    // - What is $map:02000124$?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180610000853$ 
                // - Hey, it's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison. 
                // $script:0831180610000854$ 
                // - Looks like you're short on cash. Come on back when you've got it, because this tour is worth the money! You've never seen such suffering, such misery! It builds character.
                return true;
            case 42:
                // $script:0831180610000855$ 
                // - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
                return true;
            default:
                return true;
        }
    }
}
