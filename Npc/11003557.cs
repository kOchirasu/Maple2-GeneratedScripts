using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003557: Dr. Galileo's Hologram
/// </summary>
public class _11003557 : NpcScript {
    internal _11003557(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 30:
                // $script:0907171907008984$ 
                // - The simulation is stable. Brainwaves look good. All right, let's get the ball rolling on this test!
                switch (selection) {
                    // $script:0907171907008985$
                    // - What are you doing here?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0907171907008986$
                    // - Got any advice for completing this test?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0907171907008987$ 
                // - I must admit I have a particular interest in this simulation. You see... An anonymous author from bygone days once wrote about the majesty of the $npcName:99990021$ which occurs so rarely in nature. However, the process if artificially mixing slimes to create them was legally prohibited some time ago.
                // $script:0907171907008989$ 
                // - Doesn't that just make your mind race? Why? What was so dangerous or terrible about trying to artificially create a $npcName:99990021$? That fabled splendor... I'd love to see it with my own two eyes.
                switch (selection) {
                    // $script:0907171907008990$
                    // - Sooo... What should I be doing?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0907171907008991$ 
                // - Come now, you know I'm not supposed to interfere with the test.
                switch (selection) {
                    // $script:0907171907008992$
                    // - Am I supposed to make a $npcName:99990021$?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0907171907008993$ 
                // - Err...!<font color="#909090"> <font size="20">Should I tell them? I can't interfere with the test... Of course they're bound to try mixing them sooner or later...</font>
                // $script:0907171907008994$ 
                // - ...Ahem. I suppose it would be all right if I simply explain how the machinery works.
                // $script:0907171907008995$ 
                // - The <font color="#ffd200">color meter</font> represents how many of each color of slime have been added to the machine. If the meter for any color reaches the red, that means you've exceeded the appropriate amount of slime.
                // $script:0907171907008996$ 
                // - As the mass production of artificial slimes has been outlawed for some time, the blueprints for the related machinery is quite dated and they are likely a bit imprecise. This means that being a single unit over or short of the meter's limit should not impact your success.
                // $script:0907171907008997$ 
                // - To achieve the perfect slime ratio, you'll need to get the five color meters as close to 100% as possible.
                // $script:0907171907008998$ 
                // - Ah, but there's one important thing to be aware of. The slimes come in three different sizes. <b>The larger the slime you squash, the faster the gauge fills up!</b> Good luck achieving the perfect color ratio!
                return true;
            default:
                return true;
        }
    }
}
