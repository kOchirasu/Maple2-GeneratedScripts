using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003529: Galileo
/// </summary>
public class _11003529 : NpcScript {
    internal _11003529(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0824002407008893$ 
                // - Need something?
                return true;
            case 30:
                // $script:0824002407008894$ 
                // - Welcome to the Xenon Systems Research Lab. I want to thank you for joining our study. It wasn't easy finding a guild to participate in our experiment, but I suspect you just might enjoy it!
                // $script:0906182007008914$ 
                // - Do you have any questions?
                switch (selection) {
                    // $script:0906182007008915$
                    // - What's the Xenon System?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0906182007008916$
                    // - Why do you need guild members for your test?
                    case 1:
                        Id = 41;
                        return false;
                    // $script:0906182007008917$
                    // - What's this newfangled "virtual reality" thing?
                    case 2:
                        Id = 51;
                        return false;
                    // $script:0906182007008918$
                    // - I'm ready to get my VR on!
                    case 3:
                        Id = 61;
                        return false;
                }
                return true;
            case 31:
                // $script:0906182007008919$ 
                // - The Xenon System is a combat simulation conducted in virtual reality based on the premise of psychic resonance. In layman's terms, it's an array of minds working in harmony with a computer to create a virtual world.
                // $script:0906182007008920$ 
                // - Essentially, the computer draws on the memories of everyone connected to create a simulated world that is almost indistinguishable from reality. This simulation is the perfect place to safely run all manner of tests.
                // $script:0906182007008921$ 
                // - You may already be familiar with our technology's predecessor. Have you ever participated in a Chaos Raid? 
                switch (selection) {
                    // $script:0906182007008922$
                    // - I've participated before.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0906182007008923$
                    // - Nope, never.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0906182007008924$ 
                // - I see! Yes, you carry yourself like someone who has overcome great trials.
                switch (selection) {
                    // $script:0906182007008925$
                    // - It wasn't that big of a deal.
                    case 0:
                        Id = 34;
                        return false;
                    // $script:0906182007008926$
                    // - Uhh. Thank... you...?
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0906182007008927$ 
                // - Ah, is that so? If I was still young and lithe like you, I'd be running headfirst into danger at every opportunity. You really should take on the challenge, at least once.
                switch (selection) {
                    // $script:0906182007008928$
                    // - Maybe I'll give it a go.
                    case 0:
                        Id = 34;
                        return false;
                    // $script:0906182007008929$
                    // - That's nice.
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0906182007008930$ 
                // - Ermm... In any case, we've learned a great deal by analyzing data about individuals participating in Chaos Raids, such as how shared hardships lead to team bonding, which in turn lead to greater cooperation, and greater success in battle.
                // $script:0906182007008931$ 
                // - However, as scientific tools, the Chaos Raid simulations are inferior. They are little more than a glorified entertainment system, if I'm being honest.
                // $script:0906182007008932$ 
                // - But now with the Xenon System, we can expose our guinea pi–errm, volunteers, to all sorts of situations, and conduct studies of real scientific value! It truly is a technological marvel.
                // $script:0906182007008933$ 
                // - The possibilities are endless! Everyone from the Royal Guard to the fire brigade can train in real-world situation without risk. Adventurers can visit places they never dreamed of. And I can finally take a vacation without ever leaving the lab! Of course, none of this would be possible without the support of our generous benefactor $npcName:11000264[gender:0]$.
                // $script:0906182007008934$ 
                // - Do you have any more questions?
                switch (selection) {
                    // $script:0906182007008935$
                    // - Why do you need guild members for your test?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0906182007008936$
                    // - What's this newfangled "virtual reality" thing?
                    case 1:
                        Id = 51;
                        return false;
                    // $script:0906182007008937$
                    // - I'm ready to get my VR on!
                    case 2:
                        Id = 61;
                        return false;
                }
                return true;
            case 41:
                // $script:0906182007008938$ 
                // - I wanted to put together a group study with a shared history, one conducive to cooperation.
                // $script:0906182007008939$ 
                // - After all, the greatest achievements in history come when a group of likeminded individuals unite behind a common cause.
                // $script:0906182007008940$ 
                // - There's no better example of this in everyday life than the communal efforts of guilds. I thought them a fitting subject of my test.
                // $script:0906182007008941$ 
                // - I hear we're offering an excellent compensation package for the study, although payroll is not my department. Personally, I think it's reward enough have contributed to the advancement of science, and to try out our amazing simulation. But whatever your motives, thank you for participating! 
                // $script:0906182007008942$ 
                // - Do you have any more questions?
                switch (selection) {
                    // $script:0906182007008943$
                    // - What's the Xenon System?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0906182007008944$
                    // - What's this newfangled "virtual reality" thing?
                    case 1:
                        Id = 51;
                        return false;
                    // $script:0906182007008945$
                    // - I'm ready to get my VR on!
                    case 2:
                        Id = 61;
                        return false;
                }
                return true;
            case 51:
                // $script:0906182007008946$ 
                // - Virtual reality is a simulated experience designed to believably replicate the real world. Each curated scenario is run on a separate computer server or "Link."
                // $script:0906182007008947$ 
                // - Each Link consists of a unique environment with its own hand-tailored objective.
                // $script:0906182007008948$ 
                // - Your goal, for the purposes of the study, is to cooperate with your guild members and complete the assigned objective.
                // $script:0906182007008949$ 
                // - I have to warn you, our simulations still have some kinks that need working out... You may run into situations or foes that are impossible to overcome, even with your substantial abilities. At such times, you'll need to input override codes provided by the lab.
                // $script:0906182007008950$ 
                // - <font color="#ffd200">Override Code</font> items are sold by your <font color="#ffd200">Guild Supply Merchant</font>. I wish we could give them away for free, but these little technological wonders are incredibly sophisticated and costly to produce.
                // $script:0906182007008951$ 
                // - As I've said, the various Links are all still under active development. As you proceed to complete the objectives of each simulation in order, we will analyze the data we collect, and use it to fine-tune the subsequent Links.
                // $script:0906182007008952$ 
                // - There's still a great deal of science to be done. I hope we can depend on your ongoing contribution!
                // $script:0906182007008953$ 
                // - Do you have any more questions?
                switch (selection) {
                    // $script:0906182007008954$
                    // - What's the Xenon System?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0906182007008955$
                    // - Why do you need guild members for your test?
                    case 1:
                        Id = 41;
                        return false;
                    // $script:0906182007008956$
                    // - I'm ready to get my VR on!
                    case 2:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0906182007008957$ 
                // - Wonderful. I've already booted up the system. When you're ready to access the Link, please enter one of the simulation pods.
                // $script:0906182007008958$ 
                // - There's no need to be nervous. Nothing in this simulation can inflict any <i>permanent</i> harm. That said, the study will be meaningless unless you take the scenario seriously!
                return true;
            default:
                return true;
        }
    }
}
