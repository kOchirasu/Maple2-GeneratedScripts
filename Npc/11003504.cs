using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003504: Wooji
/// </summary>
public class _11003504 : NpcScript {
    internal _11003504(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115008990$ 
                // - What is it?
                return true;
            case 30:
                // $script:0816160115008993$ 
                // - There are lots of hungry $itemPlural:61000002$ here. I'm here to capture one as a pet.
                switch (selection) {
                    // $script:0816160115008994$
                    // - Who's your little friend?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0816160115008995$
                    // - Did you come here alone?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0816160115008996$ 
                // - This is my $item:61000005$. We're traveling together. Say hello, $item:61000005$.
                switch (selection) {
                    // $script:0816160115008997$
                    // - Hello, Duckling.
                    case 0:
                        Id = 34;
                        return false;
                    // $script:0816160115008998$
                    // - Why are you traveling with a duckling?
                    case 1:
                        Id = 35;
                        return false;
                }
                return true;
            case 32:
                // $script:0816160115008999$ 
                // - No, it's just me and my $item:61000005$ on the open road! Though I did bump into my childhood friend $npcName:11003506[gender:1]$. Small world, isn't it?
                return true;
            case 34:
                // $script:0816160115009000$ 
                // - I guess my little $item:61000005$ is feeling shy.
                return true;
            case 35:
                // $script:0816160115009001$ 
                // - $item:61000005$ and I are training. I'm going to be a great pet master someday!
                return true;
            default:
                return true;
        }
    }
}
